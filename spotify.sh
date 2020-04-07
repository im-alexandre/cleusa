#!/bin/bash

spotify --uri=spotify:playlist:3JiQZbQF3QVzbbOLVsOOnu 1>/dev/null 2>&1 &
sleep 2.5
curl -X "PUT" "https://api.spotify.com/v1/me/player/play?device_id=$SPOTIFY_DEVICE_ID" --data "{\"context_uri\":\"spotify:playlist:3JiQZbQF3QVzbbOLVsOOnu\",\"offset\":{\"position\":0},\"position_ms\":5000}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN_SPOTIFY_API"