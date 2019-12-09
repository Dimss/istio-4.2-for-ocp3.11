images = ["docker.io/jaegertracing/jaeger-operator:1.13.1",
          "docker.io/jaegertracing/jaeger-operator:1.13.1",
          "quay.io/kiali/kiali-operator:v1.0.0",
          "registry.redhat.io/openshift-service-mesh/istio-rhel8-operator:1.0.0",
          "docker.io/jaegertracing/all-in-one:1.13",
          "docker.io/kiali/kiali:v1.10.0",
          "docker.io/openshift/oauth-proxy:latest",
          "docker.io/jaegertracing/all-in-one:1.13",
          "docker.io/kiali/kiali:v1.10.0",
          "docker.io/openshift/oauth-proxy:latest",
          "registry.redhat.io/openshift-service-mesh/citadel-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/galley-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/grafana-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/mixer-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/pilot-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/prometheus-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/proxyv2-rhel8:1.0.0",
          "registry.redhat.io/openshift-service-mesh/sidecar-injector-rhel8:1.0.0",
          "registry.redhat.io/openshift4/ose-oauth-proxy:4.1",
          "registry.redhat.io/openshift-service-mesh/proxy-init-rhel7:latest"]
private_repo = "docker.io/dimssss"
res = []
for i in images:
    image_array = i.split("/")
    pull_object = {"pull_image": i, "tag_image": private_repo + "/" + image_array[2]}
    res.append(pull_object)

print ("################# Docker pull #################")
for r in res:
    print ("docker pull "+r['pull_image'])
print ("################# Docker pull #################")

print ("################# Docker tag #################")
for r in res:
    print ("docker tag "+r['pull_image'] + " " + r['tag_image'])
print ("################# Docker tag #################")

print ("################# Docker push#################")
for r in res:
    print ("docker push "+r['pull_image'] + " " + r['tag_image'])
print ("################# Docker push #################")