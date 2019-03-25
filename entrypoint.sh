#!/usr/bin/env bash


case $1 in
    'deploy') python ecs_deployer/run.py ;;
    * ) exec $@ ;;
esac