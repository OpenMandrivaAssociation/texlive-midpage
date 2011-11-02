Name:		texlive-midpage
Version:	1.1a
Release:	1
Summary:	Environment for vertical centring
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/midpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midpage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The environment will centre text, if immediately preceded and
followed by \clearpage.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/midpage/midpage.sty
%doc %{_texmfdistdir}/doc/latex/midpage/midpage.pdf
%doc %{_texmfdistdir}/doc/latex/midpage/midpage.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
