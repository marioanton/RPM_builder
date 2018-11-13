%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.0.1
%endif

Name:       azure-metrics-exporter
Version:        %{_verstr}
Release:        1%{?dist}
Summary:    Azure Metrics Exporter
License:    BEDE

%description
 Azure Metrics Exporter
 
%prep
# nothing to do here

%build
# nothing to do here

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 azure-metrics-exporter %{buildroot}/usr/bin/azure-metrics-exporter

%files
/usr/bin/azure-metrics-exporter

%changelog
# let skip this for now
