#!/bin/sh

if ! spotifycli --playbackstatus 2> /dev/null | grep -q "▶"; then
    echo ""
else
    echo ""
fi
