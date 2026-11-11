import { env, isApiConfigured } from '../config/env'
import type { ApiErrorBody } from '../types/common'

/**
 * Base HTTP client. It contains NO endpoints on purpose.
 * Each feature service (chat, stocks, portfolio...) will call `apiRequest`
 * only after Danial confirms the endpoint, method and formats.
 */
export class ApiError extends Error {
  status: number
  code?: string

  constructor(message: string, status: number, code?: string) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.code = code
  }
}

export class ApiNotConfiguredError extends Error {
  constructor() {
    super('Backend URL is not configured yet (VITE_API_BASE_URL is empty).')
    this.name = 'ApiNotConfiguredError'
  }
}

interface RequestOptions {
  method?: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'
  body?: unknown
  signal?: AbortSignal
}

export async function apiRequest<T>(path: string, options: RequestOptions = {}): Promise<T> {
  if (!isApiConfigured) throw new ApiNotConfiguredError()

  const response = await fetch(`${env.apiBaseUrl}${path}`, {
    method: options.method ?? 'GET',
    headers: options.body ? { 'Content-Type': 'application/json' } : undefined,
    body: options.body ? JSON.stringify(options.body) : undefined,
    signal: options.signal,
    // Authentication method is still to be agreed with Danial.
  })

  if (!response.ok) {
    let body: Partial<ApiErrorBody> = {}
    try {
      body = (await response.json()) as Partial<ApiErrorBody>
    } catch {
      /* response had no JSON body */
    }
    throw new ApiError(body.message ?? `Request failed (${response.status})`, response.status, body.code)
  }

  return (await response.json()) as T
}
