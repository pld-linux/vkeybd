Summary:	Virtual Keyboard
Summary(pl):	Wirtualne klawisze
Name:		vkeybd
Version:	0.1.15
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.alsa-project.org/~iwai/%{name}-%{version}.tar.gz
# Source0-md5:	cf5112b4119ee21be7a819533777ba01
Source1:	%{name}rc
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-Makefile.patch
URL:		http://www.alsa-project.org/alsa.html
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
#BuildRequires:	ladcca-devel >= 0.3.1
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a virtual keyboard for AWE, MIDI and ALSA drivers. It's a
simple fake of a MIDI keyboard.

%description -l pl
Wirtualne klawisze dla sterowników AWE, MIDI i ALSA. Program "udaje"
klawisze syntezatora MIDI.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

%{__make} \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} install-all \
	OPTFLAGS="%{rpmcflags}"

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/vkeybd
install -c %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install -c %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/vkeybd
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
