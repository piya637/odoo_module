/** @odoo-module **/

import {CharField} from "@web/views/fields/char/char_field";
import {registry} from "@web/core/registry";
import {Component} from "@odoo/owl";
import {CopyButton} from "@web/core/copy_button/copy_button";
import {_t} from "@web/core/l10n/translation";
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {evaluateBooleanExpr} from "@web/core/py_js/py";
import {omit} from "@web/core/utils/objects";

export class CustomCopyClipboardField extends Component {
    static template = "priya_test.CustomCopyClipboardField";
    static components = {Field: CharField, CopyButton};
    static props = {
        ...standardFieldProps,
        string: {type: String, optional: true},
        disabledExpr: {type: String, optional: true},
        iconClass: {type: String, optional: true},
        buttonStyle: {type: String, optional: true},
    };

    setup() {
        this.copyText = this.props.string || _t("Copy");
        this.successText = _t("Copied!");
    }

    get copyButtonClassName() {
        const baseClass = "o_btn_custom_copy";
        const style = this.props.buttonStyle || "outline-secondary";
        return `${baseClass} btn-${style}`;
    }

    get fieldProps() {
        return omit(this.props, "string", "disabledExpr", "iconClass", "buttonStyle");
    }

    get copyButtonIcon() {
        return this.props.iconClass || "fa-clipboard";
    }

    get value() {
        return this.props.record.data[this.props.name] || "";
    }

    get disabled() {
        return this.props.disabledExpr
            ? evaluateBooleanExpr(
                  this.props.disabledExpr,
                  this.props.record.evalContextWithVirtualIds
              )
            : false;
    }
}

export const customCopyClipboardField = {
    component: CustomCopyClipboardField,
    displayName: _t("Custom Copy to Clipboard"),
    supportedTypes: ["char"],
    extractProps: ({attrs}) => {
        return {
            string: attrs.string,
            disabledExpr: attrs.disabled,
            iconClass: attrs.icon || "fa-clipboard",
            buttonStyle: attrs.button_style || "outline-secondary",
        };
    },
};

registry.category("fields").add("CustomCopyClipboard", customCopyClipboardField);
