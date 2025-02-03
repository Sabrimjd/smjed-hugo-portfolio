#!/bin/bash
killall hugo
hugo server --baseURL="https://smjed.net/" --bind=192.168.31.215 --disableFastRender --environment production --appendPort=false &
