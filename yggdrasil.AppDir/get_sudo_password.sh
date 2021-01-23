#!/bin/sh
ENTRY=`zenity --password`
case $? in
    0)
        echo "Password : `echo $ENTRY | cut -d'|' -f1`";;
    1)
        echo "Stop login.";;
    -1)
        echo "An unexpected error has occurred.";;
esac