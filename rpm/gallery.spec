%global _metainfodir %{_datadir}/metainfo

Name:           kirigami2gallery
Version:        23.04.17
Release:        1%{?dist}
Summary:        Kirigami component gallery application

License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/sdk/kirigami-gallery
Source0: %{name}-%{version}.tar.bz2

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
Custom:
  Repo: https://invent.kde.org/sdk/kirigami-gallery
  PackagingRepo: https://github.com/sailfishos-chum/kirigami-gallery

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

# adjust Exec command in .desktop
sed -i "s|Exec=kirigami2gallery|Exec=qt-runner /usr/bin/kirigami2gallery|g" \
    %{buildroot}/%{_datadir}/applications/org.kde.kirigami2.gallery.desktop
echo -e "X-Nemo-Single-Instance=no\nX-Nemo-Application-Type=no-invoker\n\n[X-Sailjail]\nSandboxing=Disabled" >> \
     %{buildroot}/%{_datadir}/applications/org.kde.kirigami2.gallery.desktop


%files
%{_bindir}/%{name}

%{_datadir}/applications/org.kde.kirigami2.gallery.desktop
%{_datadir}/locale
