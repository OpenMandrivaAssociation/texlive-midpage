Name:		texlive-midpage
Version:	17484
Release:	1
Summary:	Environment for vertical centring
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/midpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midpage.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The environment will centre text, if immediately preceded and
followed by \clearpage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/midpage/midpage.sty
%doc %{_texmfdistdir}/doc/latex/midpage/midpage.pdf
%doc %{_texmfdistdir}/doc/latex/midpage/midpage.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
