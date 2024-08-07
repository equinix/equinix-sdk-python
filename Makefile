.PHONY: all pull fetch patch generate clean codegen docs move-other patch-post fmt test stage

CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)

GIT_ORG=equinix
GIT_REPO=equinix-sdk-python
PACKAGE_VERSION=$(shell cat version)
USER_AGENT=${GIT_REPO}/${PACKAGE_VERSION}

OPENAPI_IMAGE_TAG=v7.4.0
OPENAPI_IMAGE=openapitools/openapi-generator-cli:${OPENAPI_IMAGE_TAG}
CRI=docker # nerdctl
OPENAPI_GENERATOR=${CRI} run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/local ${OPENAPI_IMAGE}
SPEC_FETCHER=${CRI} run --rm -u ${CURRENT_UID}:${CURRENT_GID} -v $(CURDIR):/workdir --entrypoint sh mikefarah/yq:4.30.8 script/download_spec.sh

SPEC_BASE_DIR=spec/services
TEMPLATE_BASE_DIR=templates/services
CODE_BASE_DIR=services

onboard-service:
	script/onboard_service.sh

generate-all:
	for makefile in $(shell set -x; ls -1 Makefile.* | sort -n); do \
		make -f $$makefile generate;\
	done

stage:
	test -d .git && git add --intent-to-add .
