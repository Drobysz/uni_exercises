start() {
	python3 -m venv tp2_env
	source tp2_env/bin/activate
	export PYTHONPATH="$PYTHONPATH:$(pwd)"
	python3 -m pip install -r requirements.txt
	python3 main.py
}

clean() {
	if [ ! -z "$(ls -A "imgs")" ]; then
		rm imgs/*
	fi
}

launch() {
	clean
	python3 main.py
}

reset() {
	if [ -d 'tp2_env' ]; then
		clean
		source tp2_env/bin/activate
    	export PYTHONPATH="$PYTHONPATH:$(pwd)"
		python3 main.py
	else
		echo "Initially, you should activate the programm before being able to reset it!"
	fi
}

delete() {
	clean
	rm -rf tp2_env
	rm -rf helpers/__pycache__
}

case "$1" in
  start)
    start
    ;;
  clean)
    clean
    ;;
  launch)
	launch
	;;
  reset)
    reset
    ;;
  delete)
    delete
    ;;
  help)
	echo "Accessible commands: start | launch | clean | reset | delete | help"
	;;
  *)
    echo "Unknown command: $1"
    echo "Accessible commands: start | launch | clean | reset | delete | help"
    exit 1
    ;;
esac