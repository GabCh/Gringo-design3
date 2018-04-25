#!/bin/sh
rsync -av --exclude 'venv*' --exclude '.git*' --delete . design3@design-whitecat.local:app
