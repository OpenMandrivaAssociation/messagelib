#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define olddevname %mklibname KF6MessageLib -d
%define devname %mklibname KPim6MessageLib -d

Name: plasma6-messagelib
Version:	24.02.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/messagelib/-/archive/%{gitbranch}/messagelib-%{gitbranchd}.tar.bz2#/messagelib-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/messagelib-%{version}.tar.xz
%endif
Summary: KDE library for message handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgme)
BuildRequires: cmake(Qca-qt6)
BuildRequires: sasl-devel
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KF6TextAddonsWidgets)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: cmake(KPim6GrantleeTheme)
BuildRequires: cmake(KPim6AkonadiContactCore)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6AkonadiNotes)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6LdapCore)
BuildRequires: cmake(KPim6Libkleo)
BuildRequires: cmake(KPim6Mbox)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6TextEdit)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KPim6Gravatar)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: boost-devel
BuildRequires: pkgconfig(poppler-qt6)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
Conflicts: messageviewer < 2:16.08.3-3
Conflicts: kmail < 3:17.04.0
Conflicts: kdepim-addons < 3:17.04.0
Obsoletes: %{mklibname KF6MessageComposer} < %{EVRD}
Obsoletes: %{mklibname KF6MessageCore} < %{EVRD}
Obsoletes: %{mklibname KF6MessageList} < %{EVRD}
Obsoletes: %{mklibname KF6MessageViewer} < %{EVRD}
Obsoletes: %{mklibname KF6TemplateParser} < %{EVRD}
Obsoletes: %{mklibname KF6MimeTreeParser} < %{EVRD}
Obsoletes: %{mklibname KF6WebEngineViewer} < %{EVRD}

%description
KDE library for message handling.

%define major 6
%dependinglibpackage KPim6MessageComposer %{major}

%dependinglibpackage KPim6MessageCore %{major}

%dependinglibpackage KPim6MessageList %{major}

%dependinglibpackage KPim6MessageViewer %{major}

%dependinglibpackage KPim6TemplateParser %{major}

%dependinglibpackage KPim6MimeTreeParser %{major}

%dependinglibpackage KPim6WebEngineViewer %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{mklibname KPim6MessageComposer} = %{EVRD}
Requires: %{mklibname KPim6MessageCore} = %{EVRD}
Requires: %{mklibname KPim6MessageList} = %{EVRD}
Requires: %{mklibname KPim6MessageViewer} = %{EVRD}
Requires: %{mklibname KPim6TemplateParser} = %{EVRD}
Requires: %{mklibname KPim6MimeTreeParser} = %{EVRD}
Requires: %{mklibname KPim6WebEngineViewer} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n messagelib-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libmessagecomposer6
%find_lang libmessagecore6
%find_lang libmessagelist6
%find_lang libmessageviewer6
%find_lang libmimetreeparser6
%find_lang libtemplateparser6
%find_lang libwebengineviewer6
%find_lang libmessagecomposer6
%find_lang libmessagecore6
%find_lang libmessagelist6
%find_lang libmimetreeparser6
%find_lang libtemplateparser6
%find_lang libwebengineviewer6
cat *.lang >%{name}.lang


%files -f %{name}.lang
%{_libdir}/qt6/plugins/pim6/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
%{_libdir}/qt6/plugins/pim6/messageviewer/kf6/ktexttemplate/messageviewer_ktexttemplate_extension.so
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
%{_datadir}/qlogging-categories6/messagelib.categories
%{_datadir}/qlogging-categories6/messagelib.renamecategories
%{_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/knotifications6/messageviewer.notifyrc
%{_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
