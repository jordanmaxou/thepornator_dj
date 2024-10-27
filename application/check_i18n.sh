#!/usr/bin/env bash

STATUS=0;

echo;
echo "Running i18n check!"

while read line; do
    if [[ ! -z "`msgattrib --only-fuzzy $line`" ]]; then
        echo "Found fuzzy messages in $line";
        msgattrib --only-fuzzy $line;
        echo;

        STATUS=1;
    fi

    if [[ ! -z "`msgattrib --only-obsolete $line`" ]]; then
        echo "Found obsolete messages in $line";
        msgattrib --only-obsolete $line
        echo;
        STATUS=1;
    fi

    if [[ ! -z "`msgattrib --untranslated $line`" ]]; then
        echo "Found untranslated messages in $line";
        msgattrib --untranslated $line;
        echo;
        STATUS=1;
    fi

    done < <(find ./locale/ -name *.po)

exit $STATUS;
