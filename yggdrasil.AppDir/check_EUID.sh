#!/bin/bash
(( EUID == 0 )) && is_root=0
# (( EUID != 0 )) && is_root=1
echo $is_root