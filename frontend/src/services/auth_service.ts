// frontend/src/services/auth_service.ts

interface LoginPayload {
  username: string; // Email
  password: string;
}

interface SignupPayload {
  email: string;
  password: string;
  software_background?: string;
  hardware_robotics_background?: string;
}

interface AuthResponse {
  access_token: string;
  token_type: string;
}

interface UserProfile {
  id: string;
  email: string;
  software_background?: string;
  hardware_robotics_background?: string;
}

const BACKEND_API_URL = process.env.REACT_APP_BACKEND_API_URL || "http://localhost:8000";
const TOKEN_KEY = 'accessToken'; // Key for storing token in localStorage

export const AuthService = {
  getToken(): string | null {
    return localStorage.getItem(TOKEN_KEY);
  },

  setToken(token: string): void {
    localStorage.setItem(TOKEN_KEY, token);
  },

  removeToken(): void {
    localStorage.removeItem(TOKEN_KEY);
  },

  isAuthenticated(): boolean {
    return !!this.getToken();
  },

  async login(payload: LoginPayload): Promise<AuthResponse> {
    try {
      const formBody = new URLSearchParams();
      formBody.append("username", payload.username);
      formBody.append("password", payload.password);

      const response = await fetch(`${BACKEND_API_URL}/auth/signin`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formBody.toString(),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Login failed');
      }

      const data: AuthResponse = await response.json();
      this.setToken(data.access_token);
      localStorage.setItem('mockAccessToken', data.access_token); // For ChapterDisplay mock
      return data;
    } catch (error: any) {
      console.error("Login error:", error);
      throw error;
    }
  },

  async signup(payload: SignupPayload): Promise<UserProfile> {
    try {
      const response = await fetch(`${BACKEND_API_URL}/auth/signup`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Signup failed');
      }

      const data: UserProfile = await response.json();
      // Optionally log in user immediately after signup
      // await this.login({ username: payload.email, password: payload.password });
      return data;
    } catch (error: any) {
      console.error("Signup error:", error);
      throw error;
    }
  },

  async getProfile(): Promise<UserProfile> {
    const token = this.getToken();
    if (!token) {
      throw new Error("No access token found.");
    }

    try {
      const response = await fetch(`${BACKEND_API_URL}/auth/me`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        if (response.status === 401) {
          this.removeToken(); // Token might be expired or invalid
        }
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to fetch profile');
      }

      return await response.json();
    } catch (error: any) {
      console.error("Profile fetch error:", error);
      throw error;
    }
  },

  logout(): void {
    this.removeToken();
    localStorage.removeItem('mockAccessToken'); // For ChapterDisplay mock
  },
};
