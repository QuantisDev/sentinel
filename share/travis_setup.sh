#!/bin/bash
set -evx

mkdir ~/.quantisnetcore

# safety check
if [ ! -f ~/.quantisnetcore/.quantisnet.conf ]; then
  cp share/quantisnet.conf.example ~/.quantisnetcore/quantisnet.conf
fi
