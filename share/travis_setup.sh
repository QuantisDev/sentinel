#!/bin/bash
set -evx

mkdir ~/.energicore

# safety check
if [ ! -f ~/.energicore/.energi.conf ]; then
  cp share/energi.conf.example ~/.energicore/dash.conf
fi
