
```markdown
# 📱 Bot de Emergencia para Android

Esta app permite enviar alertas con ubicación a un grupo de Telegram, ya sea presionando un botón de emergencia o mediante el acelerómetro. A continuación, te explicamos cómo compilarla e instalarla en tu dispositivo Android.

---

## 🚀 PASOS PARA INSTALAR TU APP EN ANDROID

### 1. ⚙️ Instalar dependencias en Linux (Ubuntu recomendado)

```bash
sudo apt update && sudo apt install -y \
    python3-pip \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    python3-setuptools \
    python3-virtualenv \
    libffi-dev \
    libssl-dev \
    build-essential \
    libncurses5 \
    libsqlite3-dev \
    libjpeg-dev \
    zlib1g-dev \
    pkg-config
```

> 📌 Requiere Linux. Si estás en Windows, lo ideal es usar [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) con Ubuntu o una VM.

---

### 2. 🐍 Crea un entorno virtual y actívalo

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

---

### 3. 📦 Instala Buildozer

```bash
pip install buildozer
```

---

### 4. 🏗️ Crea el archivo de configuración

Ejecuta desde tu carpeta `bot-emergencia/`:

```bash
buildozer init
```

Esto creará un archivo llamado `buildozer.spec`.

---

### 5. ✏️ Edita `buildozer.spec`

Abre `buildozer.spec` y modifica las siguientes líneas:

```ini
title = BotEmergencia
package.name = botemergencia
package.domain = org.tuseguridad

source.include_exts = py,kv,png,jpg,ttf
requirements = python3,kivy,plyer,geopy,python-telegram-bot

android.permissions = INTERNET, ACCESS_FINE_LOCATION
```

---

### 6. ⚙️ Compila tu APK

Asegúrate de estar en la raíz del proyecto (donde está `main.py`) y ejecuta:

```bash
buildozer -v android debug
```

☕ Esto puede tardar bastante la primera vez. Buildozer descargará el NDK, SDK y demás herramientas necesarias.

---

### 7. 📲 Transfiere el APK a tu celular

El archivo generado estará en:

```bash
bin/botemergencia-0.1-debug.apk
```

Puedes transferirlo usando:

- Cable USB  
- AirDrop (si estás en Mac/Linux + Android)  
- Telegram Web  
- Google Drive  

---

### 8. 🛡️ Instala en tu Android

1. Activa **"Orígenes desconocidos"** en tu Android:  
   `Ajustes → Seguridad → Permitir instalación de apps de fuentes desconocidas.`
2. Abre el APK e instálalo.

---

### 9. 🚨 Pruébala

1. Ingresa el token de tu bot de Telegram y el `chat_id` o `@grupo`.
2. Presiona el botón de prueba.
3. Simula un movimiento fuerte para probar el acelerómetro.
4. Toca el botón oculto (abajo a la derecha) para enviar la alerta manual.

---

## 📬 ¿Dudas o mejoras?

Pull requests y issues son bienvenidos. ¡Gracias por probar este proyecto!

---
