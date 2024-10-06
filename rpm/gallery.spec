%global _metainfodir %{_datadir}/metainfo

Name:           kirigami2gallery
Version:        24.08.1
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
BuildRequires:  python(abi) >= 3.0.0
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
 
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-kitemmodels-devel

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
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
%cmake_kf6
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
