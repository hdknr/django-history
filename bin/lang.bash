BASE="$HOME"
export PATH="$BASE/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

for D in `\ls $BASE/.anyenv/envs`; do
    export PATH="$BASE/.anyenv/envs/$D/shims:$PATH"
done

function DJ()
{
    PARAMS="$@"; [ -n "$PARAMS" ] || PARAMS="shell";
    C=$PWD;
    while [ "$C" != / ]; do
        [ -f "$C/manage.py" ] && { python $C/manage.py $PARAMS ; break; };
        C=`dirname $C`
    done;
}

function MD(){
    if [ "$1" = "" ]; then
        DJ histories for-day > ~/Downloads/for-day.md
    else
        DJ histories md-chrome $@ | pbcopy;
    fi
}

function JL(){
    PYTHONPATH=$PWD:$PYTHONPATH DJANGO_SETTINGS_MODULE=app.settings jupyter lab --notebook-dir  $1
}
