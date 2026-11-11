import type { DataMeta } from '../../types/common'

const freshnessLabel: Record<NonNullable<DataMeta['freshness']>, string> = {
  realtime: 'Real-time',
  delayed: 'Delayed data',
  historical: 'Historical data',
}

/**
 * Shown under every financial result (brief section 4).
 * It displays only what the backend actually provided. Nothing is guessed.
 */
export function DataSourceFooter({ meta }: { meta?: DataMeta }) {
  if (!meta) return null

  const items: { label: string; value: string }[] = []
  if (meta.source) items.push({ label: 'Source', value: meta.source })
  if (meta.timestamp) items.push({ label: 'As of', value: new Date(meta.timestamp).toLocaleString() })
  if (meta.reportingPeriod) items.push({ label: 'Reporting period', value: meta.reportingPeriod })
  if (meta.freshness) {
    const delay = meta.freshness === 'delayed' && meta.delayMinutes ? ` (~${meta.delayMinutes} min)` : ''
    items.push({ label: 'Data type', value: freshnessLabel[meta.freshness] + delay })
  }

  const hasNotes = (meta.assumptions?.length ?? 0) > 0 || (meta.limitations?.length ?? 0) > 0
  if (items.length === 0 && !hasNotes && !meta.isSimulation) return null

  return (
    <footer className="mt-4 space-y-2 border-t border-navy-600/60 pt-3 text-xs text-ink-500">
      {meta.isSimulation && (
        <p className="inline-block rounded-md bg-warn/15 px-2 py-1 font-medium text-warn">
          Simulated result. Not a guaranteed return.
        </p>
      )}
      {items.length > 0 && (
        <dl className="flex flex-wrap gap-x-5 gap-y-1">
          {items.map((i) => (
            <div key={i.label} className="flex gap-1">
              <dt className="font-medium text-ink-300">{i.label}:</dt>
              <dd>{i.value}</dd>
            </div>
          ))}
        </dl>
      )}
      {meta.assumptions && meta.assumptions.length > 0 && (
        <div>
          <p className="font-medium text-ink-300">Assumptions</p>
          <ul className="list-disc pl-4">
            {meta.assumptions.map((a) => (
              <li key={a}>{a}</li>
            ))}
          </ul>
        </div>
      )}
      {meta.limitations && meta.limitations.length > 0 && (
        <div>
          <p className="font-medium text-ink-300">Limitations</p>
          <ul className="list-disc pl-4">
            {meta.limitations.map((l) => (
              <li key={l}>{l}</li>
            ))}
          </ul>
        </div>
      )}
    </footer>
  )
}
