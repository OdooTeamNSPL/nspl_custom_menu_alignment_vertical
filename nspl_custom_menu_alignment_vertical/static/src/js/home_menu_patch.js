/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { HomeMenu } from "@web_enterprise/webclient/home_menu/home_menu";
import { rpc } from "@web/core/network/rpc";
import { hasTouch } from "@web/core/browser/feature_detection";
import { onMounted } from "@odoo/owl";

patch(HomeMenu.prototype, {
    setup() {
        super.setup?.();

        this.state.apps_by_category = {};
        this.state.menuLayout = "default"; // Will be populated via RPC

        onMounted(async () => {
            if (!hasTouch()) {
                this._focusInput?.();
            }

            try {
                // Get the selected menu layout (default / vertical / horizontal)
                const layoutResponse = await rpc("/web/session/get_company_menu_layout_vertical", {});
                const layout = layoutResponse?.layout || "default";
                this.state.menuLayout = layout;

                if (layout === "vertical") {
                    const categoryMap = await rpc("/web/custom_app_categories", {});
                    const apps = this.props.apps;

                    const enrichedApps = apps.map((app) => {
                        const moduleName = app.xmlid?.split(".")[0];
                        const category = categoryMap[moduleName] || "Others";
                        return { ...app, category };
                    });

                    const grouped = {};
                    for (const app of enrichedApps) {
                        const cat = app.category;
                        if (!grouped[cat]) grouped[cat] = [];
                        grouped[cat].push(app);
                    }

                    this.state.apps_by_category = grouped;
                }

            } catch (err) {
                console.error("Error loading menu layout or categories", err);
            }
        });
    },

    get displayedApps() {
        // Use grouped apps only for vertical/horizontal layouts
        if (this.state.menuLayout === "vertical") {
            return this.state.apps_by_category;
        }
        return this.props.apps;
    },
});
