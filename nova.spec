#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : nova
Version  : 18.0.2
Release  : 149
URL      : http://tarballs.openstack.org/nova/nova-18.0.2.tar.gz
Source0  : http://tarballs.openstack.org/nova/nova-18.0.2.tar.gz
Source1  : nova.tmpfiles
Source99 : http://tarballs.openstack.org/nova/nova-18.0.2.tar.gz.asc
Summary  : Cloud computing fabric controller
Group    : Development/Tools
License  : Apache-2.0
Requires: nova-bin = %{version}-%{release}
Requires: nova-config = %{version}-%{release}
Requires: nova-license = %{version}-%{release}
Requires: nova-python = %{version}-%{release}
Requires: nova-python3 = %{version}-%{release}
Requires: Babel
Requires: Jinja2
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: Sphinx
Requires: WebOb
Requires: castellan
Requires: cryptography
Requires: cursive
Requires: decorator
Requires: enum34
Requires: eventlet
Requires: futures
Requires: greenlet
Requires: iso8601
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: lxml
Requires: microversion_parse
Requires: netaddr
Requires: netifaces
Requires: openstackdocstheme
Requires: os-api-ref
Requires: os-brick
Requires: os-service-types
Requires: os-traits
Requires: os-win
Requires: os-xenapi
Requires: os_vif
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
Requires: python-dateutil
Requires: python-glanceclient
Requires: python-neutronclient
Requires: reno
Requires: requests
Requires: retrying
Requires: rfc3986
Requires: setuptools
Requires: six
Requires: sphinx-feature-classification
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: taskflow
Requires: tooz
Requires: websockify
Requires: zVMCloudConnector
BuildRequires : buildreq-distutils3
BuildRequires : cursive
BuildRequires : microversion_parse
BuildRequires : os-traits
BuildRequires : os_vif
BuildRequires : pbr
BuildRequires : prettytable
BuildRequires : pypowervm
BuildRequires : zVMCloudConnector

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the nova package.
Group: Binaries
Requires: nova-config = %{version}-%{release}
Requires: nova-license = %{version}-%{release}

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
Requires: nova-python3 = %{version}-%{release}

%description python
python components for the nova package.


%package python3
Summary: python3 components for the nova package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nova package.


%prep
%setup -q -n nova-18.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540823343
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nova
cp LICENSE %{buildroot}/usr/share/package-licenses/nova/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nova/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
