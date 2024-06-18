%global _metainfodir %{_datadir}/metainfo

Name:           kirigami2gallery
Version:        23.08.5
Release:        1%{?dist}
Summary:        Kirigami component gallery application

License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/sdk/kirigami-gallery
Source0: %{name}-%{version}.tar.bz2

Source10: kirigami-logo.png

%{?opt_kf5_default_filter}

#BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  opt-kf5-rpm-macros
 
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kirigami-addons
BuildRequires:  opt-kf5-kitemmodels-devel

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-qt5-linguist

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-kirigami2%{_isa} 
Requires: opt-kf5-kirigami-addons
Requires: opt-kf5-kitemmodels
Requires: qt-runner
Requires: breeze-icons

%description
Kirigami component gallery application

PackageName: Kirigami Demo Gallery
Type: desktop-application
Categories:
 - Utilities
Icon: https://raw.githubusercontent.com/sailfishos-chum/kirigami-gallery/main/rpm/kirigami-logo.png
Custom:
  Repo: https://invent.kde.org/sdk/kirigami-gallery
  PackagingRepo: https://github.com/sailfishos-chum/kirigami-gallery

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%cmake_build

%install
%cmake_install

# copy icons
install -p -m644 -D %{SOURCE10} \
	%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/kirigami-gallery.png
install -p -m644 -D %{SOURCE10} \
	%{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/kirigami-gallery.png
install -p -m644 -D %{SOURCE10} \
	%{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/kirigami-gallery.png
install -p -m644 -D %{SOURCE10} \
	%{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/kirigami-gallery.png

# adjust Exec command in .desktop
sed -i "s|Exec=kirigami2gallery|Exec=qt-runner /usr/bin/kirigami2gallery|g" \
    %{buildroot}/%{_datadir}/applications/org.kde.kirigami2.gallery.desktop
# swap icon
sed -i "s|Icon=preferences-desktop-theme|Icon=kirigami-gallery|g" \
    %{buildroot}/%{_datadir}/applications/org.kde.kirigami2.gallery.desktop
# add sfos settings
echo -e "X-Nemo-Single-Instance=no\nX-Nemo-Application-Type=no-invoker\n\n[X-Sailjail]\nSandboxing=Disabled" >> \
     %{buildroot}/%{_datadir}/applications/org.kde.kirigami2.gallery.desktop


%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/kirigami-gallery.png
%{_datadir}/applications/org.kde.kirigami2.gallery.desktop
%{_datadir}/locale
