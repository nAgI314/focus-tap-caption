import { StyleSheet } from 'react-native';

import { Stack } from 'expo-router';

export default function HomeScreen() {
  return (
  <>
  <Stack.Screen options={{ title: 'Heren NVILA TEST' }} />
    {/* <ThemedView style={styles.titleContainer}>
    </ThemedView>
    <ThemedView style={styles.stepContainer}>
      <ThemedText>
        Edit <ThemedText type="defaultSemiBold">app/(tabs)/index.tsx</ThemedText> to see changes.
        Press{' '}
        <ThemedText type="defaultSemiBold">
          {Platform.select({
            ios: 'cmd + d',
            android: 'cmd + m',
            web: 'F12',
          })}
        </ThemedText>{' '}
        to open developer tools.
      </ThemedText>
    </ThemedView> */}
    </>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
