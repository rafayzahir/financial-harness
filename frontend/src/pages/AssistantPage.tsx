import { Send } from 'lucide-react'
import { Card } from '../components/ui/Card'
import { PageHeader } from '../components/ui/PageHeader'
import { ApiPendingState } from '../components/ui/StateViews'

// Example questions from the brief. They are only suggestions to read, not AI answers.
const exampleQuestions = [
  'Analyze Apple stock.',
  'Compare Apple and Microsoft.',
  'Explain the latest company earnings.',
  'Show technical indicators for a stock.',
  'Compare two investment scenarios.',
  'Analyze my portfolio.',
  'What happens if a stock price changes by 10%?',
]

export function AssistantPage() {
  return (
    <>
      <PageHeader title="AI Assistant" description="Ask stock market questions in plain language." />
      <div className="grid gap-6 xl:grid-cols-[1fr_320px]">
        <Card className="flex min-h-[420px] flex-col">
          <div className="flex-1" aria-live="polite">
            <ApiPendingState dependency="Danial: chat API. Hamid: AI response JSON structure" />
          </div>
          <form
            className="mt-4 flex gap-2"
            onSubmit={(e) => {
              e.preventDefault()
            }}
          >
            <label htmlFor="chat-input" className="sr-only">
              Ask a question
            </label>
            <input
              id="chat-input"
              disabled
              placeholder="Chat is not available yet"
              className="min-w-0 flex-1 rounded-xl border border-navy-600 bg-navy-900 px-4 py-2.5 text-sm text-ink-100 placeholder:text-ink-500 disabled:cursor-not-allowed disabled:opacity-60"
            />
            <button
              type="submit"
              disabled
              aria-label="Send"
              className="grid w-11 place-items-center rounded-xl bg-brand-600 text-white disabled:cursor-not-allowed disabled:opacity-50"
            >
              <Send size={18} />
            </button>
          </form>
        </Card>

        <Card title="Things you can ask" subtitle="Examples from the project brief">
          <ul className="space-y-2 text-sm text-ink-300">
            {exampleQuestions.map((q) => (
              <li key={q} className="rounded-lg bg-navy-900 px-3 py-2">
                {q}
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </>
  )
}
