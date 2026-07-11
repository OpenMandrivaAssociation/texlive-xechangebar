%global tl_name xechangebar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	An extension of package changebar that can be used with XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xechangebar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xechangebar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xechangebar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends package changebar so it can be used with XeLaTeX. It
introduces the new option xetex for use with XeLaTeX. Everything else
remains the same and users should consult the original documentation for
usage information.

