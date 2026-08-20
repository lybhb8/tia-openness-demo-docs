# Minimal makefile for Sphinx documentation

SPHINXBUILD   = sphinx-build
SPHINXOPTS    =
SPHINXPROJ    = TIAPortalOpenness
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

serve:
	@python -m http.server 8000 --directory _build/html

watch:
	@while true; do $(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" -W --keep-going; sleep 5; done
