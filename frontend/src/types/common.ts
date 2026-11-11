/**
 * PROPOSED shared "transparency" shape for every financial result.
 * This is a proposal to agree with Danial and Hamid. It is NOT a final API contract.
 * Every field is optional because the UI must show only what the backend really sends.
 */
export interface DataMeta {
  source?: string
  /** ISO timestamp of when the data was produced */
  timestamp?: string
  reportingPeriod?: string
  assumptions?: string[]
  limitations?: string[]
  /** 'realtime' only when the backend explicitly says so */
  freshness?: 'realtime' | 'delayed' | 'historical'
  delayMinutes?: number
  isSimulation?: boolean
}

/** Standard error the UI can show. Real shape to be confirmed with Danial. */
export interface ApiErrorBody {
  message: string
  code?: string
}
