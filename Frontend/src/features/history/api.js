import client from "../../api/client";

export const getRecentHistory = (page = 1, limit = 8) => {
    return client.get("/history/my_history", {
        params: {
            page_no: page,
            limit: limit
        }
    });
};