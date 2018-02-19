%define major 5
%define libname %mklibname KF5MessageLib %{major}
%define devname %mklibname KF5MessageLib -d

Name: messagelib
Epoch: 3
Version:	 17.12.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	3
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for message handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: sasl-devel
BuildRequires: cmake(KF5AkonadiSearch)
BuildRequires: cmake(KF5AkonadiNotes)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(KF5SendLater)
BuildRequires: cmake(KF5Mbox)
BuildRequires: cmake(KF5Gravatar)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5MailTransport)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Grantlee5)
BuildRequires: boost-devel
BuildRequires: pkgconfig(poppler-qt5)
Conflicts: messageviewer < 2:16.08.3-3
Conflicts: kmail < 3:17.04.0
Conflicts: kdepim-addons < 3:17.04.0

%description
KDE library for message handling.

%define major 5
%dependinglibpackage KF5MessageComposer %{major}
%dependinglibpackage KF5MessageCore %{major}
%dependinglibpackage KF5MessageList %{major}
%dependinglibpackage KF5MessageViewer %{major}
%dependinglibpackage KF5TemplateParser %{major}
%dependinglibpackage KF5MimeTreeParser %{major}
%dependinglibpackage KF5WebEngineViewer %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{mklibname KF5MessageComposer %{major}} = %{EVRD}
Requires: %{mklibname KF5MessageCore %{major}} = %{EVRD}
Requires: %{mklibname KF5MessageList %{major}} = %{EVRD}
Requires: %{mklibname KF5MessageViewer %{major}} = %{EVRD}
Requires: %{mklibname KF5TemplateParser %{major}} = %{EVRD}
Requires: %{mklibname KF5MimeTreeParser %{major}} = %{EVRD}
Requires: %{mklibname KF5WebEngineViewer %{major}} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libmessagecomposer
%find_lang libmessagecore
%find_lang libmessagelist
%find_lang libmessageviewer
%find_lang libmimetreeparser
%find_lang libtemplateparser
%find_lang libwebengineviewer
%find_lang libmessagecomposer
%find_lang libmessagecore
%find_lang libmessagelist
%find_lang libmessageviewer
%find_lang libmimetreeparser
%find_lang libtemplateparser
%find_lang libwebengineviewer
cat *.lang >%{name}.lang


%files -f %{name}.lang
%{_libdir}/qt5/plugins/messageviewer/*.so
%{_libdir}/qt5/plugins/messageviewer/grantlee/*/messageviewer_grantlee_extension.so
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
%{_datadir}/kconf_update/messageviewer.upd
%{_sysconfdir}/xdg/messagelib.categories
%{_sysconfdir}/xdg/messagelib.renamecategories
%{_sysconfdir}/xdg/messageviewer_header_themes.knsrc
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/knotifications5/messageviewer.notifyrc
%{_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
