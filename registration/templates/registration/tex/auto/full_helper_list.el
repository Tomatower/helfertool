(TeX-add-style-hook
 "full_helper_list"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "a4paper" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8x") ("fontenc" "T1") ("babel" "ngerman") ("caption" "tableposition=top") ("geometry" "top=1.5cm" "bottom=1.5cm" "left=1.7cm" "right=1.5cm")))
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl10"
    "inputenc"
    "fontenc"
    "babel"
    "longtable"
    "fancyhdr"
    "caption"
    "geometry"))
 :latex)

