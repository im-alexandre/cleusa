#!/bin/bash

spotify --uri=spotify:playlist:3JiQZbQF3QVzbbOLVsOOnu 1>/dev/null 2>&1 &

dbus-send \
    --print-reply \
    --dest=org.mpris.MediaPlayer2.spotify \
    /org/mpris/MediaPlayer2 \
    org.mpris.MediaPlayer2.Player.PlayPause &

sleep 3
curl -X "PUT" "https://api.spotify.com/v1/me/player/play?device_id=75eb06287c3c0b940ac0c69e6c3931b5202b744f" --data "{\"context_uri\":\"spotify:playlist:3JiQZbQF3QVzbbOLVsOOnu\",\"offset\":{\"position\":0},\"position_ms\":5000}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQAYpupgkWSzExoZCe0IpSw1_nAzubpY2mFOqUvZFP9iiem4-6Z4O9LY7rbWthtrtJZ6ppYprI-VQaxiJdsW3ECixhliVtF22AyyygbznAe6cPeGnTE3rHYLAJXzA4xmuMw1xLd8W4rO2jxQb9gwSoBw0nD3Qg"

curl -X "PUT" "https://api.spotify.com/v1/me/player/volume?volume_percent=100&device_id=75eb06287c3c0b940ac0c69e6c3931b5202b744f" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQAYpupgkWSzExoZCe0IpSw1_nAzubpY2mFOqUvZFP9iiem4-6Z4O9LY7rbWthtrtJZ6ppYprI-VQaxiJdsW3ECixhliVtF22AyyygbznAe6cPeGnTE3rHYLAJXzA4xmuMw1xLd8W4rO2jxQb9gwSoBw0nD3Qg"