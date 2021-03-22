import requestHandler from "./requestHandler";
import auth from "./auth";

const api = {
  ...requestHandler,

  async getTasks() {
    return await this.get("/api/tasks");
  },
};
api.auth = auth(api);

export default api;
