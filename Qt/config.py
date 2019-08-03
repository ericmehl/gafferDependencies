{

	"downloads" : [

		"https://download.qt.io/archive/qt/5.6/5.6.1/single/qt-everywhere-opensource-src-5.6.1.tar.xz"

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
			" -skip qtconnectivity"
			" -skip qtwebengine"
			" -skip qt3d"
			" -skip qtdeclarative"
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

		"variables" : {

			"PATH" : "%PATH%;{buildDir}\\lib;{buildDir}\\bin",

		},

		"commands" : [

			"copy {buildDir}\\lib\\zlib.lib {buildDir}\\lib\\zdll.lib",
			# "copy {buildDir}\\lib\\libpng.lib {buildDir}\\lib\\libpng16.lib",
			"copy {buildDir}\\lib\\jpeg.lib {buildDir}\\lib\\libjpeg.lib",
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
				" -skip qt3d"
				" -skip qtdeclarative"
				" -nomake examples"
				" -nomake tests"
				" -system-zlib"
				" -no-openssl"
				" -I {buildDir}\\include"
				" -L {buildDir}\\lib",
			"jom.exe",
			"jom.exe install",

		]
	}

}
