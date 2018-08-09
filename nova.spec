#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : nova
Version  : 17.0.5
Release  : 145
URL      : http://tarballs.openstack.org/nova/nova-17.0.5.tar.gz
Source0  : http://tarballs.openstack.org/nova/nova-17.0.5.tar.gz
Source1  : nova.tmpfiles
Source99 : http://tarballs.openstack.org/nova/nova-17.0.5.tar.gz.asc
Summary  : Cloud computing fabric controller
Group    : Development/Tools
License  : Apache-2.0
Requires: nova-bin
Requires: nova-config
Requires: nova-python3
Requires: nova-license
Requires: nova-python
Requires: Babel
Requires: Jinja2
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: WebOb
Requires: castellan
Requires: cryptography
Requires: cursive
Requires: decorator
Requires: enum34
Requires: eventlet
Requires: greenlet
Requires: iso8601
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: lxml
Requires: netaddr
Requires: netifaces
Requires: os-brick
Requires: os-service-types
Requires: os-traits
Requires: os-win
Requires: os-xenapi
Requires: oslo.cache
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.privsep
Requires: oslo.reports
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: oslo.versionedobjects
Requires: osprofiler
Requires: paramiko
Requires: pbr
Requires: prettytable
Requires: psutil
Requires: pypowervm
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-neutronclient
Requires: requests
Requires: rfc3986
Requires: setuptools
Requires: six
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: taskflow
Requires: tooz
Requires: websockify
BuildRequires : buildreq-distutils3
BuildRequires : cursive
BuildRequires : os-traits
BuildRequires : pbr
BuildRequires : prettytable
BuildRequires : pypowervm

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the nova package.
Group: Binaries
Requires: nova-config
Requires: nova-license

%description bin
bin components for the nova package.


%package config
Summary: config components for the nova package.
Group: Default

%description config
config components for the nova package.


%package license
Summary: license components for the nova package.
Group: Default

%description license
license components for the nova package.


%package python
Summary: python components for the nova package.
Group: Default
Requires: nova-python3

%description python
python components for the nova package.


%package python3
Summary: python3 components for the nova package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nova package.


%prep
%setup -q -n nova-17.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533821747
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/nova
cp LICENSE %{buildroot}/usr/share/doc/nova/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/nova.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nova-api
/usr/bin/nova-api-metadata
/usr/bin/nova-api-os-compute
/usr/bin/nova-api-wsgi
/usr/bin/nova-cells
/usr/bin/nova-compute
/usr/bin/nova-conductor
/usr/bin/nova-console
/usr/bin/nova-consoleauth
/usr/bin/nova-dhcpbridge
/usr/bin/nova-manage
/usr/bin/nova-metadata-wsgi
/usr/bin/nova-network
/usr/bin/nova-novncproxy
/usr/bin/nova-placement-api
/usr/bin/nova-policy
/usr/bin/nova-rootwrap
/usr/bin/nova-rootwrap-daemon
/usr/bin/nova-scheduler
/usr/bin/nova-serialproxy
/usr/bin/nova-spicehtml5proxy
/usr/bin/nova-status
/usr/bin/nova-xvpvncproxy

%files config
%defattr(-,root,root,-)
%config /usr/etc/nova/api-paste.ini
%config /usr/etc/nova/rootwrap.conf
%config /usr/etc/nova/rootwrap.d/api-metadata.filters
%config /usr/etc/nova/rootwrap.d/compute.filters
%config /usr/etc/nova/rootwrap.d/network.filters
/usr/lib/tmpfiles.d/nova.conf

%files license
%defattr(-,root,root,-)
/usr/share/doc/nova/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
