%define major 5
%define olddevname %mklibname KF5MessageLib -d
%define devname %mklibname KPim5MessageLib -d

Name: messagelib
Epoch: 3
Version:	23.08.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# Drop support for old versions of KTextAddons to make
# rpm's cmake dependency generator happy
Patch0: messagelib-23.04.1-drop-ktextaddons-1.2.patch
Summary: KDE library for message handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Positioning)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5WebChannel)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgme)
BuildRequires: cmake(Qca-qt5)
BuildRequires: sasl-devel
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5AkonadiContact)
BuildRequires: cmake(KPim5AkonadiMime)
BuildRequires: cmake(KPim5AkonadiNotes)
BuildRequires: cmake(KPim5AkonadiSearch)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KPim5Gravatar)
BuildRequires: cmake(KPim5MailTransport)
BuildRequires: cmake(KPim5IdentityManagement)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(Grantlee5)
BuildRequires: cmake(KPim5GrantleeTheme)
BuildRequires: cmake(KPim5Ldap)
BuildRequires: cmake(KPim5Libkleo)
BuildRequires: cmake(KPim5Mbox)
BuildRequires: cmake(KPim5TextEdit)
BuildRequires: cmake(KPim5Libkdepim)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KPim5PimCommonAkonadi)
BuildRequires: boost-devel
BuildRequires: pkgconfig(poppler-qt5)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Conflicts: messageviewer < 2:16.08.3-3
Conflicts: kmail < 3:17.04.0
Conflicts: kdepim-addons < 3:17.04.0
Obsoletes: %{mklibname KF5MessageComposer} < %{EVRD}
Obsoletes: %{mklibname KF5MessageCore} < %{EVRD}
Obsoletes: %{mklibname KF5MessageList} < %{EVRD}
Obsoletes: %{mklibname KF5MessageViewer} < %{EVRD}
Obsoletes: %{mklibname KF5TemplateParser} < %{EVRD}
Obsoletes: %{mklibname KF5MimeTreeParser} < %{EVRD}
Obsoletes: %{mklibname KF5WebEngineViewer} < %{EVRD}

%description
KDE library for message handling.

%define major 5
%dependinglibpackage KPim5MessageComposer %{major}
%dependinglibpackage KPim5MessageCore %{major}
%dependinglibpackage KPim5MessageList %{major}
%dependinglibpackage KPim5MessageViewer %{major}
%dependinglibpackage KPim5TemplateParser %{major}
%dependinglibpackage KPim5MimeTreeParser %{major}
%dependinglibpackage KPim5WebEngineViewer %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{mklibname KPim5MessageComposer} = %{EVRD}
Requires: %{mklibname KPim5MessageCore} = %{EVRD}
Requires: %{mklibname KPim5MessageList} = %{EVRD}
Requires: %{mklibname KPim5MessageViewer} = %{EVRD}
Requires: %{mklibname KPim5TemplateParser} = %{EVRD}
Requires: %{mklibname KPim5MimeTreeParser} = %{EVRD}
Requires: %{mklibname KPim5WebEngineViewer} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
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
%find_lang libmimetreeparser
%find_lang libtemplateparser
%find_lang libwebengineviewer
cat *.lang >%{name}.lang


%files -f %{name}.lang
%{_libdir}/qt5/plugins/pim5/messageviewer/grantlee/*/messageviewer_grantlee_extension.so
%{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
%{_datadir}/qlogging-categories5/messagelib.categories
%{_datadir}/qlogging-categories5/messagelib.renamecategories
%{_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/knotifications5/messageviewer.notifyrc
%{_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{tags,qch}
