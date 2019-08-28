{

	"downloads" : [

		"https://download.qt.io/archive/qt/5.11/5.11.2/single/qt-everywhere-src-5.11.2.tar.xz"

	],

	"license" : "LICENSE.LGPLv21",

	"commands" : [

		"tar -xf ../qt561-webkit.tgz",

		"./configure"
			" -prefix {buildDir}"
			" -plugindir {buildDir}/qt/plugins"
			" -release"
			" -opensource -confirm-license"
			" -no-rpath -no-gtkstyle"
			" -no-audio-backend -no-dbus"
			" -skip qt3d"
			" -skip qtcharts"
			" -skip qtconnectivity"
			" -skip qtdatavis3d"
			" -skip qtdeclarative"
			" -skip qtpurchasing"
			" -skip qtgamepad"
			" -skip qtspeech"
			" -skip qtwebchannel"
			" -skip qtwebengine"
			" -no-libudev"
			" -no-gstreamer"
			" -no-icu"
			" -qt-pcre"
			" -nomake examples"
			" -nomake tests"
			" {extraArgs}"
			" -I {buildDir}/include -I {buildDir}/include/freetype2"
			" -L {buildDir}/lib"
			" -c++std c++11"
		,

		"make -j {jobs}",
		"make install",

	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib",

		},

		"variables" : {

			"extraArgs" : "-qt-xcb",

		},

	},

	"platform:osx" : {

		"variables" : {

			"extraArgs" : "-no-freetype -platform macx-clang",

		},

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "%ROOT_DIR%\\Qt\\working\\qt-everywhere-src-5.11.2\\qtbase\\lib;{buildDir}\\lib;{buildDir}\\bin;%PATH%",

		},

		"commands" : [

			"copy {buildDir}\\lib\\zlib.lib {buildDir}\\lib\\zdll.lib",
			"copy {buildDir}\\lib\\libpng16.lib {buildDir}\\lib\\libpng.lib",
			"copy {buildDir}\\lib\\jpeg.lib {buildDir}\\lib\\libjpeg.lib",
			# help Qt find the right zlib.dll
			"copy {buildDir}\\bin\\zlib.dll %ROOT_DIR%\\Qt\\working\\qt-everywhere-src-5.11.2\\qtbase\\bin\\zlib.dll",
			"call configure.bat"
				" -prefix {buildDir}"
				" -plugindir {buildDir}\\qt\\plugins"
				" -release"
				" -opensource"
				" -confirm-license"
				" -opengl desktop"
				" -no-angle"
				" -no-dbus"
				" -skip qtconnectivity"
				" -skip qtwebengine"
				" -skip qtdatavisualization"
				" -skip qttexttospeech"
				" -skip qt3d"
				" -nomake examples"
				" -nomake tests"
				" -system-zlib"
				" -I {buildDir}\\include"
				" -L {buildDir}\\lib",
			"jom.exe",
			"jom.exe install",

		]
	}

}
