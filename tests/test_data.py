import json


def test_data(app, client):
    del app
    res = client.get('/data')
    assert res.status_code == 200
    expected = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          -3.4751429886991616,
          50.72716575022636
        ],
        "type": "Point"
      }
    }
  ]
}
    assert expected == json.loads(res.get_data(as_text=True))