# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define section free
%define _basename javacc

Name:           javacc3
Version:        3.2
Release:        %mkrel 4
Epoch:          0
Summary:        A parser/scanner generator for java
License:        BSD
Source0:	javacc-3.2-src.tar.gz
Source1:	javacc
Source2:	jjdoc
Source3:	jjtree
Patch0:		javacc3-source_1.4.patch
URL:            https://javacc.dev.java.net/
Group:          Development/Java
BuildRoot:      %{_tmppath}/%{_basename}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires:	jpackage-utils >= 0:1.5
BuildRequires:	java-devel java-rpmbuild
BuildRequires:	ant, /bin/bash

%description 
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

%package manual
Summary:        Manual for %{_basename}
Group:          Development/Java

%description manual
Manual for %{_basename}.

%package demo
Summary:        Examples for %{_basename}
Group:          Development/Java

%description demo
Examples for %{_basename}.

%prep
%setup -q -n %{_basename}-%{version}
%patch0 -p1
cp %{SOURCE1} javacc
cp %{SOURCE2} jjdoc
cp %{SOURCE3} jjtree
mv www/doc .

%build
ant \
  -Dversion=%{version} \
  jar

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 bin/lib/%{_basename}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 javacc jjdoc jjtree $RPM_BUILD_ROOT/usr/bin
install -d -m 755 $RPM_BUILD_ROOT/usr/share/%{name}
cp -pr examples $RPM_BUILD_ROOT/usr/share/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_javadir}/*.jar
%doc LICENSE README
%defattr(0755,root,root,0755)
/usr/bin/*

%files manual
%defattr(0644,root,root,0755)
%doc doc/*

%files demo
%defattr(0644,root,root,0755)
/usr/share/%{name}/*

