/**
 * Frontend settings read from `.env` (never put private API keys here).
 * Danial will tell us the real backend URL. Until then it stays empty.
 */
export const env = {
  apiBaseUrl: (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? '',
}

export const isApiConfigured = env.apiBaseUrl.length > 0
