%define major 5
%define libname %mklibname KF5MessageLib %{major}
%define devname %mklibname KF5MessageLib -d

Name: messagelib
Version:	16.04.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
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
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5JobWidgets)

%description
KDE library for message handling

%define major 5
%dependinglibpackage KF5MessageComposer %{major}
%dependinglibpackage KF5MessageCore %{major}
%dependinglibpackage KF5MessageList %{major}
%dependinglibpackage KF5MessageViewer %{major}
%dependinglibpackage KF5TemplateParser %{major}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{mklibname KF5MessageComposer %{major}} = %{EVRD}
Requires: %{mklibname KF5MessageCore %{major}} = %{EVRD}
Requires: %{mklibname KF5MessageList %{major}} = %{EVRD}
Requires: %{mklibname KF5MessageViewer %{major}} = %{EVRD}
Requires: %{mklibname KF5TemplateParser %{major}} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
cd ../
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/libmessageviewer
%{_datadir}/messagelist
%{_datadir}/messageviewer
%{_datadir}/kconf_update/messageviewer.upd
%{_sysconfdir}/xdg/messagelib.categories
%{_sysconfdir}/xdg/messageviewer_header_themes.knsrc
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/knotifications5/messageviewer.notifyrc

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
