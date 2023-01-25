This repository accompanies Stack Overflow answer <https://stackoverflow.com/a/75238026/147356>.

## Installing on Rasbpian

You will need to install some dependencies:

```
sudo apt update
sudo apt install -y python3-{fastapi,pygame,requests,rpi.gpio} uvicorn
```

And provide your own sound file named `fanfare.mp3`.

## Starting the example API

The file `apiserver.py` is a simple API with a single endpoint used for testing the alarm code. It responds to the `/endpoint` path with the value contained in `endpoint.value` (or 0, if the file does not exist). To run the API:

```
uvicorn apiserver:app
```

This will start the API on `http://localhost:8000`.

## Wiring

The code in `checker.py` expects the following GPIO connections:

- A button on GPIO4
- An LED on GPIO17

## Running the code

If you've wired things up correctly and started the API server (or modified the code to use your own API instead), you can start things up by running:

```
python checker.py
```

If you're using the example API server, you can change the return value by echoing a new value to the `endpoint.value` file:

```
echo $RANDOM > endpoint.value
```

This will cause `checker.py` to detect a change the next time it runs, triggering the music and lights.
