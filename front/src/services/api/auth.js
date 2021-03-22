export default function (api) {
  return {
    async login(data) {
      const response = await api.post("/api/auth/login", data, true);
      if (api.status === 200) {
        api.authToken = response.access_token;
        return response.user;
      } else {
        return null;
      }
    },
  };
}
