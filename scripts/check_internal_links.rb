#!/usr/bin/env ruby

require "nokogiri"
require "pathname"
require "uri"

site_root = Pathname.new(ARGV.fetch(0, "_site")).expand_path
documents = Dir.glob(site_root.join("**/*.html")).sort
document_cache = {}
errors = []

resolve_target = lambda do |source, raw_path|
  decoded = URI::DEFAULT_PARSER.unescape(raw_path)
  base = decoded.start_with?("/") ? site_root.join(decoded.delete_prefix("/")) : Pathname.new(source).dirname.join(decoded)
  expanded = base.expand_path
  next nil unless expanded.to_s.start_with?(site_root.to_s)

  candidates = [expanded]
  candidates << expanded.join("index.html") if File.directory?(expanded) || File.extname(expanded.to_s).empty?
  candidates << Pathname.new("#{expanded}.html") if File.extname(expanded.to_s).empty?
  candidates.find(&:file?)
end

documents.each do |source|
  document = Nokogiri::HTML(File.read(source))
  selectors = {
    "a[href]" => "href",
    "img[src]" => "src",
    "script[src]" => "src",
    "link[href]" => "href",
    "iframe[src]" => "src"
  }

  selectors.each do |selector, attribute|
    document.css(selector).each do |node|
      value = node[attribute].to_s.strip
      next if value.empty? || value.start_with?("#", "//", "mailto:", "tel:", "javascript:", "data:")
      next if value.match?(%r{\Ahttps?://}i)

      path, fragment = value.split("#", 2)
      path = source if path.nil? || path.empty?
      path = path.split("?", 2).first
      target = resolve_target.call(source, path)

      unless target
        errors << "#{Pathname.new(source).relative_path_from(site_root)}: missing #{value}"
        next
      end

      next if fragment.nil? || fragment.empty? || target.extname.downcase != ".html"

      target_document = document_cache[target.to_s] ||= Nokogiri::HTML(File.read(target))
      fragment_id = URI::DEFAULT_PARSER.unescape(fragment)
      anchor = target_document.at_css(%([id="#{fragment_id.gsub('"', '\\"')}"])) ||
               target_document.at_css(%([name="#{fragment_id.gsub('"', '\\"')}"]))
      errors << "#{Pathname.new(source).relative_path_from(site_root)}: missing anchor #{value}" unless anchor
    end
  end
end

if errors.empty?
  puts "Internal link check passed (#{documents.size} HTML pages)."
else
  warn errors.uniq.join("\n")
  warn "Internal link check failed with #{errors.uniq.size} issue(s)."
  exit 1
end
