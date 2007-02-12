#
# Conditional build
%bcond_with	ladcca	# with LADCCA support
#
Summary:	Virtual Keyboard
Summary(pl.UTF-8):   Wirtualne klawisze
Name:		vkeybd
Version:	0.1.17
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.alsa-project.org/~iwai/%{name}-%{version}.tar.gz
# Source0-md5:	3be348329a5aac3cdc21f89458d9369a
Source1:	%{name}rc
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-lib64.patch
URL:		http://www.alsa-project.org/alsa.html
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
%{?with_ladcca:BuildRequires:	ladcca-devel >= 0.4.0}
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a virtual keyboard for AWE, MIDI and ALSA drivers. It's a
simple fake of a MIDI keyboard.

%description -l pl.UTF-8
Wirtualne klawisze dla sterowników AWE, MIDI i ALSA. Program "udaje"
klawisze syntezatora MIDI.

%prep
%setup -q -n %{name}
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif

%build
%{__make} %{?with_ladcca:USE_LADCCA=1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-all \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/vkeybd
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_pixmapsdir}/vkeybd_48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/vkeybd.png
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/vkeybd_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/vkeybd
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
