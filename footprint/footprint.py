# Footprint map: an interactive Leaflet map with a year slider showing places
# connected to my work and travel accumulating over time.
#
# This is the single source of truth. Edit the LOCATIONS list below and
# regenerate the map with:
#
#     python footprint/footprint.py
#
# (or just push a change to this file and the "Update Footprint Map" GitHub
# Action regenerates and commits the map for you).
#
# Each entry is ("year", "location"):
#   - year     : the visit year; the slider reveals a place from its first year
#   - location : geocoded via OpenStreetMap / Nominatim, so use a clear
#                "City, Country" string (add state/region when helpful)
#
# The output is written to footprint/map.html, which is embedded on the
# Personal page at /footprint/map.html.

import os
import json
import time
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Run from the repo root so the output path below is stable, regardless of the
# directory the script is launched from.
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

TIMEOUT = 5
OUTPUT = "footprint/map.html"

# --- Footprint locations (edit this list) -------------------------------------
LOCATIONS = [
    ("2026", "Glacier National Park, USA"),
    ("2026", "New Haven, CT, USA"),
    ("2026", "St. Louis, MO, USA"),
    ("2026", "New York City, NY, USA"),
    ("2025", "Kanas Lake, China"),
    ("2025", "Sailimu Lake, China"),
    ("2025", "Urumqi, China"),
    ("2025", "Manaus, Brazil"),
    ("2025", "Sao Paulo, Brazil"),
    ("2025", "Dubai, United Arab Emirates"),
    ("2025", "Chicago, IL, USA"),
    ("2025", "Cleveland, OH, USA"),
    ("2025", "Washington DC, USA"),
    ("2025", "Geneva, Switzerland"),
    ("2025", "Bern, Switzerland"),
    ("2025", "Baltimore, MD, USA"),
    ("2024", "Rostock, Germany"),
    ("2024", "Berlin, Germany"),
    ("2024", "Acadia National Park, Maine, USA"),
    ("2024", "Portland, Maine, USA"),
    ("2024", "Geneva, Switzerland"),
    ("2024", "Somkhele, South Africa"),
    ("2024", "Durban, South Africa"),
    ("2024", "Cape Town, South Africa"),
    ("2024", "Sao Paulo, Brazil"),
    ("2024", "Rio de Janeiro, Brazil"),
    ("2024", "Foz do Iguaçu, Brazil"),
    ("2024", "New Orleans, USA"),
    ("2024", "Curitiba, Brazil"),
    ("2023", "Anchorage, AK, USA"),
    ("2023", "Denali National Park, AK, USA"),
    ("2023", "Homer, AK, USA"),
    ("2023", "Seward, AK, USA"),
    ("2023", "Dallas, TX, USA"),
    ("2023", "Bandim, Guinea Bissau"),
    ("2023", "Bissau, Guinea Bissau"),
    ("2023", "Rubane Island, Guinea Bissau"),
    ("2023", "Casablanca, Morocco"),
    ("2023", "Paris, France"),
    ("2023", "Geneva, Switzerland"),
    ("2023", "Penglai, China"),
    ("2023", "Nanjing, China"),
    ("2023", "Suzhou, China"),
    ("2023", "Hangzhou, China"),
    ("2023", "Nashville, TN, USA"),
    ("2023", "Atlanta, GA, USA"),
    ("2023", "Great Smoky Mountains National Park, USA"),
    ("2022", "Geneva, Switzerland"),
    ("2022", "Lyon, France"),
    ("2022", "Orlando, FL, USA"),
    ("2021", "Geneva, Switzerland"),
    ("2020", "Chicago, IL, USA"),
    ("2019", "Philadelphia, PA, USA"),
    ("2019", "San Juan, Puerto Rico"),
    ("2019", "Toronto, Canada"),
    ("2019", "Niagara Falls, Canada"),
    ("2019", "Lake Erie, OH, USA"),
    ("2019", "Austin, TX, USA"),
    ("2018", "Ann Arbor, Michigan, USA"),
    ("2018", "Seattle, WA, USA"),
    ("2018", "Columbus, OH, USA"),
    ("2018", "Chapel Hill, NC, USA"),
    ("2018", "Shanghai, China"),
    ("2017", "London, UK"),
    ("2017", "Lima, Peru"),
    ("2017", "Cusco, Peru"),
    ("2017", "Arequipa, Peru"),
    ("2017", "Titicaca Lake, Peru"),
    ("2017", "Amazonia, Peru"),
    ("2017", "Machu Picchu, Peru"),
    ("2017", "Beijing, China"),
    ("2017", "Rocky Mountain National Park, Colorado, USA"),
    ("2017", "Denver, Colorado, USA"),
    ("2016", "Mexico City, Mexico"),
    ("2016", "Cancun, Mexico"),
    ("2016", "Merida, Mexico"),
    ("2016", "Guanajuato, Mexico"),
    ("2016", "Las Vegas, USA"),
    ("2016", "Zion National Park, USA"),
    ("2016", "Chengdu, China"),
    ("2016", "Huanglong Scenic Area, Sichuan, China"),
    ("2016", "Jiuzhaigou, China"),
    ("2015", "Salt Lake City, USA"),
    ("2015", "Yellowstone National Park, USA"),
    ("2015", "Grand Teton National Park, USA"),
    ("2015", "Shenandoah National Park, USA"),
    ("2015", "Geneva, Switzerland"),
    ("2015", "Chengdu, China"),
    ("2015", "Yingxiu, China"),
    ("2014", "Boston, MA, USA"),
    ("2014", "New York City, NY, USA"),
    ("2014", "Geneva, Switzerland"),
    ("2014", "San Diego, CA, USA"),
    ("2014", "San Francisco, CA, USA"),
    ("2014", "Los Angeles, CA, USA"),
    ("2013", "New York City, NY, USA"),
    ("2013", "Washington DC, USA"),
    ("2012", "Philadelphia, PA, USA"),
    ("2012", "Baltimore, MD, USA"),
    ("2011", "Harbin, China"),
    ("2011", "Lianyungang, China"),
    ("2011", "Changsha, China"),
    ("2010", "Hainan, China"),
    ("2010", "Changsha, China"),
    ("2010", "Fenghuang, China"),
    ("2009", "Zhangjiajie, China"),
    ("2008", "Xiamen, China"),
    ("2007", "Lushan National Park, China"),
    ("2007", "Anji, China"),
    ("2007", "Nanjing, China"),
    ("2007", "Shanghai, China"),

    # ("year", "City, Country"),
]
# ------------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Footprint</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style>
  html, body { margin: 0; height: 100%; font-family: Helvetica, Arial, sans-serif; }
  #map { position: absolute; top: 0; left: 0; right: 0; bottom: 66px; }
  #timebar { position: absolute; left: 0; right: 0; bottom: 0; height: 66px;
    box-sizing: border-box; padding: 12px 18px; background: #fff;
    border-top: 1px solid #d8e2dd; display: flex; align-items: center; gap: 14px; }
  #timebar .cap { color: #50616b; font-size: 0.85rem; white-space: nowrap; }
  #yrlabel { font-weight: 700; color: #1f5b57; min-width: 2.6em; text-align: center; }
  #yr { flex: 1; accent-color: #1f5b57; }
</style>
</head>
<body>
<div id="map"></div>
<div id="timebar">
  <span class="cap">Footprints through</span>
  <span id="yrlabel"></span>
  <input id="yr" type="range" step="1">
</div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  const PLACES = __PLACES__;
  const map = L.map("map");
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19, attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map);

  const markers = PLACES.map(function (p) {
    const m = L.marker([p.lat, p.lon])
      .bindPopup("<b>" + p.location + "</b><br>" + p.years.join(", "));
    m._first = p.first;
    return m;
  });

  if (PLACES.length) {
    map.fitBounds(L.latLngBounds(PLACES.map(function (p) { return [p.lat, p.lon]; })).pad(0.2));
  } else {
    map.setView([20, 0], 2);
  }

  const years = PLACES.map(function (p) { return p.first; });
  const minYear = years.length ? Math.min.apply(null, years) : 2018;
  const maxYear = years.length ? Math.max.apply(null, years) : 2026;
  const slider = document.getElementById("yr");
  const label = document.getElementById("yrlabel");
  slider.min = minYear; slider.max = maxYear; slider.value = maxYear;

  function render() {
    const y = +slider.value;
    label.textContent = y;
    markers.forEach(function (m) {
      if (m._first <= y) { m.addTo(map); } else { map.removeLayer(m); }
    });
  }
  slider.addEventListener("input", render);
  render();
</script>
</body>
</html>
"""


def geocode_places(locations):
    """Geocode each unique location once; collect years visited per place."""
    geocoder = Nominatim(user_agent="y-chu.github.io")
    years_by_location = {}
    for year, location in locations:
        years_by_location.setdefault(location, set()).add(int(year))

    places = []
    for location, years in years_by_location.items():
        try:
            geo = geocoder.geocode(location, timeout=TIMEOUT)
        except (GeocoderTimedOut, ValueError) as ex:
            print(f"Error: geocode failed on {location!r}: {ex}")
            continue
        except Exception as ex:
            print(f"Unhandled error on {location!r}: {ex}")
            continue
        if geo is None:
            print(f"Not found (skipped): {location!r}")
            continue
        places.append({
            "location": location,
            "lat": geo.latitude,
            "lon": geo.longitude,
            "years": sorted(years),
            "first": min(years),
        })
        print(f"{location} -> ({geo.latitude:.4f}, {geo.longitude:.4f})")
        time.sleep(1)  # respect Nominatim's ~1 request/second usage policy
    return places


def write_map(places, path=OUTPUT):
    html = HTML_TEMPLATE.replace("__PLACES__", json.dumps(places))
    with open(path, "w") as f:
        f.write(html)
    print(f"Wrote {path} with {len(places)} place(s)")


if __name__ == "__main__":
    write_map(geocode_places(LOCATIONS))
