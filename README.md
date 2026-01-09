# Domovoy Starter

A starter template for creating Home Assistant automations using [Domovoy](https://github.com/carlos-sarmiento/domovoy) and Docker.

## Step-by-Step Setup

### Step 1: Clone this repository

You can create a copy of this repository in your personal account and use it to store your automations and configuration.

### Step 2: Update `config.yaml`

Update the `config.yaml` file with your Home Assistant configuration:

**Important:** Replace the following values:
- `hass_access_token`: Your Home Assistant long-lived access token
- `hass_url`: Your Home Assistant WebSocket URL
- `timezone`: Your timezone
- `latitude` and `longitude`: Your location coordinates (used for sun-based automations)

### Step 3: Install Dependencies

We recommend using [`uv`](https://docs.astral.sh/uv/) to manage dependencies. Once it is installed in your system you can run:

```bash
uv sync
```

Although Domovoy will run inside the Docker container, we install the dependencies in this folder so your IDE can provide linting and type-checking for your automations.

### Step 4: Run Domovoy

```bash
docker run -d --name "domovoy" -v "$(pwd):/config" ghcr.io/carlos-sarmiento/domovoy:latest
```

## Creating New Apps

1. Create a new Python file in the `apps/` directory with a name ending in `_apps.py`
2. Define your app class extending `AppBase`
3. Register it using `register_app()`

Use the VS Code snippets for quick scaffolding:
- Type `app` and press Tab to create an app with config
- Type `app_no_config` and press Tab to create an app without config
- Type `register` and press Tab to register an app

## Notes

- App files must end with `_apps.py` (configurable via `app_suffix` in `config.yaml`)
- The typing stub generator apps will create `entities.pyi` and `services.pyi` files that provide autocomplete for your Home Assistant entities and services
- Type stubs are regenerated automatically when Domovoy connects to Home Assistant
