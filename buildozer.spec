[app]
title = Discord Bass
package.name = discordbass
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,numpy,pyjnius
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

